type Student = {
  id: number;
  name: string;
  email: string;
  status: "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";
};

const getStatusBadge = (status: Student["status"]) => {
  const baseClasses =
    "px-2.5 py-0.5 text-xs font-medium rounded-full inline-block";
  switch (status) {
    case "COMPLETED":
      return `${baseClasses} bg-green-100 text-green-800`;
    case "NEW":
      return `${baseClasses} bg-blue-100 text-blue-800`;
    case "ONGOING":
      return `${baseClasses} bg-yellow-100 text-yellow-800`;
    case "VISA_LODGE":
      return `${baseClasses} bg-purple-100 text-purple-800`;
    default:
      return `${baseClasses} bg-gray-100 text-gray-800`;
  }
};

interface StudentTableProps {
  students: Student[];
}

const StudentTable = ({ students = [] }: StudentTableProps) => {
  if (!Array.isArray(students)) {
    console.error("Students prop must be an array");
    return (
      <div className="text-center py-10">
        <p className="text-gray-500">Error loading students data.</p>
      </div>
    );
  }

  if (students.length === 0) {
    return (
      <div className="text-center py-10">
        <p className="text-gray-500">No students found for this filter.</p>
      </div>
    );
  }

  return (
    <div className="overflow-x-auto bg-white rounded-lg shadow">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th
              scope="col"
              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Name
            </th>
            <th
              scope="col"
              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Email
            </th>
            <th
              scope="col"
              className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
            >
              Status
            </th>
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {students.map((student) => (
            <tr key={student.id} className="hover:bg-gray-50">
              <td className="px-6 py-4 whitespace-nowrap">
                <div className="text-sm font-medium text-gray-900">{`${student.name}`}</div>
              </td>
              <td className="px-6 py-4 whitespace-nowrap">
                <div className="text-sm text-gray-600">{student.email}</div>
              </td>
              <td className="px-6 py-4 whitespace-nowrap">
                <span className={getStatusBadge(student.status)}>
                  {student.status.replace("_", " ")}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default StudentTable;
