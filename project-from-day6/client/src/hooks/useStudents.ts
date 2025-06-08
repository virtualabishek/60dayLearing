import { useState, useEffect } from "react";

export type Status = "ALL" | "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";

export type Student = {
  id: number;
  name: string;
  email: string;
  status: Exclude<Status, "ALL">;
};

export const useStudents = (status: string = "ALL") => {
  const [students, setStudents] = useState<Student[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchStudents = async () => {
      try {
        setLoading(true);
        const url =
          status === "ALL"
            ? "http://localhost:3000/student/"
            : `http://localhost:3000/student/status/${status}`;

        const response = await fetch(url);
        const result = await response.json();

        if (!result.success) {
          throw new Error(result.message);
        }

        setStudents(result.data || []);
      } catch (err) {
        setError(
          err instanceof Error ? err.message : "Failed to fetch students"
        );
      } finally {
        setLoading(false);
      }
    };

    fetchStudents();
  }, [status]);

  return { students, loading, error };
};
