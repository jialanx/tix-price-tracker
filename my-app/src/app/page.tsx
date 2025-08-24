
export default function Home() {
  return (
    <>
      <h1>Vividseats Ticket Price Tracker</h1>
      <input className="border " placeholder="Input here" />
      <button type="submit" className="m-2 bg-blue-500 text-white p-2 rounded">Submit</button>
    </>
  );

  function handleSubmit(event: React.FormEvent) {
    event.preventDefault();
    // Handle form submission logic here
  }
}
