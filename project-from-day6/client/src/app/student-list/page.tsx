"use client";
import { useState, useEffect } from "react";
import Head from "next/head";
import StudentTable from "@/components/StudentTable";
import StatusFilter from "@/components/StatusFilter";
import axios from "axios";

export type Student = {
  id: number;
  name: string;
  email: string;
  status: "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";
};

type Status = "ALL" | "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";

const StudentsPage = () => {
  const [students, setstudents] = useState<Student[]>([]);
  const [activeStatus, setActiveStatus] = useState<Status>("ALL");
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchStudents = async () => {
      console.log("Fetching student data...");
      setIsLoading(true);
      const API_URL = "http://localhost:8000/student";
      let url = "";
      if (activeStatus === "ALL") {
        url = API_URL;
      } else {
        url = `${API_URL}/status/${activeStatus.toLowerCase()}`;
      }
      try {
        const response = await axios.get(url);
        if (response.data && Array.isArray(response.data.data)) {
          setstudents(response.data.data);
        }
        // setstudents(response.data);
      } catch (error) {
        console.log(error);
        console.error("Failed to fetched students:", error);
        setstudents([]);
      } finally {
        setIsLoading(false);
      }
    };

    fetchStudents();
  }, [activeStatus]);

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

          <StatusFilter
            activeStatus={activeStatus}
            onFilterChange={setActiveStatus}
          />

          {isLoading ? (
            <div className="text-center py-10">
              <p className="text-gray-500">Loading students...</p>
            </div>
          ) : (
            <StudentTable students={students} />
          )}
        </div>
      </main>
    </>
  );
};

export default StudentsPage;
