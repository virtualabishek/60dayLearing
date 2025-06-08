// components/StatusFilter.tsx

type Status = "ALL" | "NEW" | "ONGOING" | "VISA_LODGE" | "COMPLETED";

interface StatusFilterProps {
  activeStatus: Status;
  onFilterChange: (status: Status) => void;
}

const StatusFilter = ({ activeStatus, onFilterChange }: StatusFilterProps) => {
  const statuses: Status[] = [
    "ALL",
    "NEW",
    "ONGOING",
    "VISA_LODGE",
    "COMPLETED",
  ];

  return (
    <div className="flex space-x-2 border-b border-gray-200 mb-6">
      {statuses.map((status) => (
        <button
          key={status}
          onClick={() => onFilterChange(status)}
          className={`px-4 py-2 text-sm font-medium transition-colors duration-150 ease-in-out focus:outline-none
            ${
              activeStatus === status
                ? "border-b-2 border-indigo-600 text-indigo-600"
                : "text-gray-500 hover:text-gray-700"
            }
          `}
        >
          {status.replace("_", " ")}
          {/* yo chai just for rediability, improved like VISA LODGE not VISA_LODGE */}
        </button>
      ))}
    </div>
  );
};

export default StatusFilter;
