import { initialTickets } from "@/data";
import { ticketPath } from "@/paths";
import Link from "next/link";

const TicketPage = () => {
    return (
        <div>
            <h1 className="text-lg">Hello from Ticket Page</h1>
            <div>
                {initialTickets.map((ticket) => (
                    <div key={ticket.id}>
                        <h2 className="text-lg">{ticket.title}</h2>
                        <br />
                        {/* <Link href={`/ticket/${ticket.id}`} className="text-sm underline">View</Link> */}
                        <Link href={ticketPath(ticket.id)} className="text-sm underline">View</Link>
                    </div>

                ))}
                
            </div>
        </div>
    );
}

export default TicketPage;