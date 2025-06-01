import { initialTickets } from "@/data";

type TicketPageProps = {
    params: {
        ticketid: string;
    };
}

const TicketPage = ({params}: TicketPageProps) => {
    const ticket = initialTickets.find((ticket)=> ticket.id ===params.ticketid)
    if(!ticket) {
        return <div>Ticket not found.</div>
    }
    return (
        <div>
            <h2 className="text-lg">Tickets Page {ticket.title}</h2>
            <p className="text-sm">{ticket.content}</p>
        </div>
    )
}

export default TicketPage;