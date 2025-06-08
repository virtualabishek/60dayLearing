import { Request, Response } from "express";
import { StudentStatus } from "../../generated/prisma";

export interface CreateStudentInput {
  name: string;
  password?: string;
  email?: string | null;
  status: StudentStatus;
}
import prisma from "../utils/prisma";

export default class StudentController {
  getStudentWithStatus = async (req: Request, res: Response): Promise<void> => {
    const status = req.params.status as string;
    const normalizedStatus = status
      .toUpperCase()
      .replace(/-/g, "_") as keyof typeof StudentStatus;

    if (!Object.keys(StudentStatus).includes(normalizedStatus)) {
      res.status(400).json({ success: false, message: "Invalid Status Value" });
      return;
    }

    try {
      const students = await prisma.user.findMany({
        where: {
          status: StudentStatus[normalizedStatus],
        },
      });

      res.json({ success: true, data: students });
    } catch (error) {
      console.error(error);
      res
        .status(500)
        .json({ success: false, message: "Cannot find the user with status" });
    }
  };

  addStudent = async (
    req: Request,
    res: Response,
    input: CreateStudentInput
  ): Promise<void> => {
    const { name, password, email, status } = input;
    try {
      const student = await prisma.user.create({
        data: {
          name: name,
          password: password ?? "",
          email: email ?? "",
          status: status || StudentStatus.NEW,
        },
      });
      res.json({ success: true, data: student });
    } catch (error) {
      console.log(error);
      res.status(500).json({ success: false, message: "Cannot Create" });
    }
  };
  getAllStudent = async (req: Request, res: Response): Promise<void> => {
    try {
      const page = parseInt(req.query?.page as string) || 1;
      const limit = parseInt(req.query?.limit as string) || 10;
      const sortBy = (req.query?.sortBy as string) || "name";
      const sortOrder = (req.query?.sortOrder as "asc" | "desc") || "asc";
      const allowedSortBy = ["id", "name", "email", "status"];
      if (!allowedSortBy.includes(sortBy)) {
        res
          .status(400)
          .json({ success: false, message: "Invalid sortBy parameter." });
      }
      const skip = (page - 1) * limit;
      const [students, total] = await prisma.$transaction([
        prisma.user.findMany({
          skip: skip,
          take: limit,
          orderBy: {
            [sortBy]: sortOrder,
          },
        }),
        prisma.user.count(),
      ]);
      res.status(200).json({
        success: true,
        data: students,
        pagination: {
          total,
          limit,
          page,
          totalPages: Math.ceil(total / limit),
        },
      });
    } catch (error) {
      console.error(error);
      res.status(500).json({
        success: false,
        message: "Error fetching students",
      });
    }
  };
}
