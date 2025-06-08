"use client";

import { useState, FormEvent } from "react";
import axios from "axios";

type StudentData = {
  name: string;
  email: string;
  password: string;
  status: "NEW" | "COMPLETED" | "VISA_LODGED" | "ONGOING";
};

const StudentForm = () => {
  const [formData, setFormData] = useState<StudentData>({
    name: "",
    password: "",
    email: "",
    status: "NEW",
  });

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();

    console.log("Form data to be sent to the API:", formData);

    axios
      .post("http://localhost:8000/student/add", formData)
      .then(function (response) {
        console.log(response);
        setFormData({
          name: "",
          password: "",
          email: "",
          status: "NEW",
        });
        if (response.data.success) {
          alert("Student Added!");
        } else {
          alert("Student can't add.");
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  return (
    <div className="max-w-lg mx-auto mt-10 p-8 bg-white rounded-xl shadow-md">
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">
        Add New Student
      </h2>
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label
            htmlFor="name"
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            Name
          </label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 **text-gray-900**"
          />
        </div>

        <div>
          <label
            htmlFor="password"
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            Password
          </label>
          <input
            type="password"
            id="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 **text-gray-900**"
          />
        </div>

        {/* Email Input */}
        <div>
          <label
            htmlFor="email"
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            Email Address
          </label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 **text-gray-900**"
          />
        </div>

        {/* Status Dropdown */}
        <div>
          <label
            htmlFor="status"
            className="block text-sm font-medium text-gray-700 mb-1"
          >
            Status
          </label>
          <select
            id="status"
            name="status"
            value={formData.status}
            onChange={handleChange}
            className="w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-black-900"
          >
            <option value="COMPLETED"> COMPLETED</option>
            <option value="ONGOING">ONGOING</option>
            <option value="NEW">NEW</option>
            <option value="VISA_LODGE">VISA_LODGED</option>
          </select>
        </div>

        {/* Submit Button */}
        <div>
          <button
            type="submit"
            className="w-full py-3 px-4 bg-indigo-600 text-white font-semibold rounded-md shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition duration-150 ease-in-out"
          >
            Add Student
          </button>
        </div>
      </form>
    </div>
  );
};

export default StudentForm;
