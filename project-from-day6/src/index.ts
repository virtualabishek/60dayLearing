import express from "express";
import studentRoutes from "./routes/student.routes";
const app = express();
app.use(express.json());

app.use("/student", studentRoutes);

app.get("/", (req, res) => {
  res.send("Server is running well.");
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

export default app;
