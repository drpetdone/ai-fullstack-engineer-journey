import { useEffect, useState } from "react";
import type { User } from "./types/user";
import { getUsers, createUser } from "./services/userService";

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  const fetchUsers = async () => {
    const data = await getUsers();
    setUsers(data);
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  const handleSubmit = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    await createUser(name, email);

    setName("");
    setEmail("");

    fetchUsers();
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>AI Fullstack Dashboard</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) =>
            setName(e.target.value)
          }
        />

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <button type="submit">
          Add User
        </button>
      </form>

      <hr />

      <h2>Users</h2>
      <table border={1} cellPadding={5} cellSpacing={0} style={{ width: "100%" }}>
          <thead><tr><th>ID</th><th>Name</th><th>Email</th></tr></thead>           
          <tbody>
            
       {users.map((user) => (
        
          <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
          </tr>      
         
      ))}
       </tbody>
        </table>
    </div>
  );
}

export default App;