"use client"
import { ButtonIncrement } from "@/components/button";
import { useState, useEffect } from "react";
import Link from "next/link";
import { ticketsPath } from "@/paths";

export default function Home() {
  const [count, setCount] = useState(0);
  let theme = "white";
  useEffect(()=> {
    theme="dark";
  })

  const handleMe = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <h1 className="text-lg">Home Page</h1>
      <br />
    <Link href={ticketsPath()}>Go Ticket Page</Link> <br />
      <button onClick={handleMe}>Click Me: {count}</button>
      <br />
      <ButtonIncrement />
      <br />
    </div>
  );
}
