import { useState } from "react";
import api from "../api";

export default function Auth() {
  const [isLogin, setIsLogin] = useState(true);
  const [form, setForm] = useState({ username: "", email: "", password: "" });

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (isLogin) {
        const res = await api.post("/auth/token/", {
          username: form.username,
          password: form.password,
        });
        localStorage.setItem("access", res.data.access);
        localStorage.setItem("refresh", res.data.refresh);
        alert("Logged in!");
      } else {
        await api.post("/auth/register/", form);
        alert("Registered! Now login.");
        setIsLogin(true);
      }
    } catch (err) {
      console.error(err);
      alert("Error");
    }
  };

  return (
    <div>
      <h2>{isLogin ? "Login" : "Register"}</h2>
      <form onSubmit={handleSubmit}>
        <input
          name="username"
          placeholder="Username"
          value={form.username}
          onChange={handleChange}
        />
        {!isLogin && (
          <input
            name="email"
            placeholder="Email"
            value={form.email}
            onChange={handleChange}
          />
        )}
        <input
          type="password"
          name="password"
          placeholder="Password"
          value={form.password}
          onChange={handleChange}
        />
        <button type="submit">{isLogin ? "Login" : "Register"}</button>
      </form>
      <button onClick={() => setIsLogin(!isLogin)}>
        {isLogin ? "Need an account?" : "Already have an account?"}
      </button>
    </div>
  );
}
