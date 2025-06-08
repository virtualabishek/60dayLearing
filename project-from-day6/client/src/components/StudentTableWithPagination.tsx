export type Student = {
  id: number;
  name: string;
  email: string;
  status: "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";
};

interface StudentTableProps {
  students: Student[];
  onSort: (field: string) => void;
  sortBy: string;
  sortOrder: "asc" | "desc";
}

const SortIcon = ({ direction }: { direction: "asc" | "desc" | "none" }) => {
  if (direction === "none") return null;
  return <span>{direction === "asc" ? "▲" : "▼"}</span>;
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

const StudentTable = ({
  students = [],
  onSort,
  sortBy,
  sortOrder,
}: StudentTableProps) => {
  const headers = [
    { key: "name", label: "Name" },
    { key: "email", label: "Email" },
    { key: "status", label: "Status" },
  ];

  if (students.length === 0) {
    return (
      <div className="text-center py-10">
        <p className="text-gray-500">No students found.</p>
      </div>
    );
  }

  return (
    <div className="overflow-x-auto bg-white rounded-lg shadow">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            {headers.map((header) => (
              <th
                key={header.key}
                scope="col"
                className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                onClick={() => onSort(header.key)}
              >
                <div className="flex items-center space-x-1">
                  <span>{header.label}</span>
                  <SortIcon
                    direction={sortBy === header.key ? sortOrder : "none"}
                  />
                </div>
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="bg-white divide-y divide-gray-200">
          {students.map((student) => (
            <tr key={student.id} className="hover:bg-gray-50">
              <td className="px-6 py-4 whitespace-nowrap">
                <div className="text-sm font-medium text-gray-900">
                  {student.name}
                </div>
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
