import StudentForm from "@/components/StudentForm";
import Head from "next/head";

const AddStudentPage = () => {
  return (
    <>
      <Head>
        <title>Add a New Student</title>
        <meta
          name="description"
          content="A form to add a new student to the system."
        />
      </Head>
      <main className="min-h-screen bg-gray-100 flex flex-col items-center py-10">
        <StudentForm />
      </main>
    </>
  );
};

export default AddStudentPage;
