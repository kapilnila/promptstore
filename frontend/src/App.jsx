import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Auth from "./pages/Auth";
import Prompts from "./pages/Prompts";

function App() {
  const token = localStorage.getItem("access");

  const logout = () => {
    localStorage.removeItem("access");
    localStorage.removeItem("refresh");
    window.location.href = "/";
  };

  return (
    <BrowserRouter>
      <nav>
        <Link to="/">Home</Link> | 
        {!token && <Link to="/auth">Login / Register</Link>} 
        {token && (
          <button onClick={logout}>
            Logout
          </button>
        )}
      </nav>

      <Routes>
        <Route path="/" element={<Prompts />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;

