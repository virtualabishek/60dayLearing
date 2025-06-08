"use client";
import { useState, useEffect } from "react";
import Head from "next/head";
import StudentTable from "@/components/StudentTableWithPagination";
import axios from "axios";

export type Student = {
  id: number;
  name: string;
  email: string;
  status: "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";
};

type Status = "ALL" | "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";

type PaginationData = {
  total: number;
  limit: number;
  page: number;
  totalPages: number;
};

const StudentsPage = () => {
  const [students, setStudents] = useState<Student[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [pagination, setPagination] = useState<PaginationData | null>(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [sortOrder, setSortOrder] = useState<"asc" | "desc">("asc");
  const [sortBy, setSortBy] = useState("name");

  useEffect(() => {
    const fetchStudent = async () => {
      setIsLoading(true);
      try {
        const params = new URLSearchParams({
          page: currentPage.toString(),
          limit: "5",
          sortBy: sortBy,
          sortOrder: sortOrder,
        });
        const url = `http://localhost:8000/student?${params.toString()}`;
        const response = await axios.get(url);
        if (response.data && response.data.success) {
          setStudents(response.data.data);
          setPagination(response.data.pagination);
        } else {
          setStudents([]);
          setPagination(null);
        }
      } catch (error) {
        console.error("Failed to fetch students:", error);
        setStudents([]);
        setPagination(null);
      } finally {
        setIsLoading(false);
      }
    };
    fetchStudent();
  }, [currentPage, sortBy, sortOrder]);

  const handleSort = (field: string) => {
    const newSortOrder =
      sortBy === field && sortOrder === "asc" ? "desc" : "asc";
    setSortBy(field);
    setSortOrder(newSortOrder);
    setCurrentPage(1);
  };

  return (
    <>
      <Head>
        <title>Student Dashboard</title>
        <meta
          name="description"
          content="View and manage all student records."
        />
      </Head>
      <main className="bg-gray-50 min-h-screen">
        <div className="max-w-7xl mx-auto py-10 px-4 sm:px-6 lg:px-8">
          <div className="mb-8">
            <h1 className="text-3xl font-bold text-gray-900">
              Student Dashboard
            </h1>
            <p className="mt-1 text-sm text-gray-500">
              Filter and view all student records in the system.
            </p>
          </div>

          {isLoading ? (
            <div className="text-center py-10">
              <p className="text-gray-500">Loading...</p>
            </div>
          ) : (
            <StudentTable
              students={students}
              onSort={handleSort}
              sortBy={sortBy}
              sortOrder={sortOrder}
            />
          )}
          <div className="flex items-center justify-between mt-4">
            <div>
              {pagination && (
                <p className="text-sm text-gray-700">
                  Showing page{" "}
                  <span className="font-medium">{pagination.page}</span> of{" "}
                  <span className="font-medium">{pagination.totalPages}</span>
                </p>
              )}
            </div>
            <div className="flex space-x-2">
              <button
                onClick={() => setCurrentPage((prev) => prev - 1)}
                disabled={!pagination || currentPage === 1}
                className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Previous
              </button>
              <button
                onClick={() => setCurrentPage((prev) => prev + 1)}
                disabled={!pagination || currentPage === pagination.totalPages}
                className="px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-md hover:bg-gray-50 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Next
              </button>
            </div>
          </div>
        </div>
      </main>
    </>
  );
};

export default StudentsPage;
