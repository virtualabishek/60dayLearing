import { Router } from "express";
import StudentController from "../controllers/student.controller";
import { Request, Response } from "express";

const router = Router();
const studentController = new StudentController();

router.get("/status/:status", (req: Request, res: Response) => {
  return studentController.getStudentWithStatus(req, res);
});

router.post("/add", (req: Request, res: Response) => {
  return studentController.addStudent(req, res, req.body);
});

router.get("/", (req: Request, res: Response) => {
  return studentController.getAllStudent(req, res);
});
export default router;
