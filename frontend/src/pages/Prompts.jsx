import { useEffect, useState } from "react";
import api from "../api";

export default function Prompts() {
  const [prompts, setPrompts] = useState([]);
  const [form, setForm] = useState({
    title: "",
    description: "",
    content: "",
    price: "",
    tags: "",
  });

  const loadPrompts = async () => {
    const res = await api.get("/prompts/");
    setPrompts(res.data);
  };

  useEffect(() => {
    loadPrompts();
  }, []);

  const handleChange = (e) =>
    setForm({ ...form, [e.target.name]: e.target.value });

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await api.post("/prompts/", form);
      setForm({ title: "", description: "", content: "", price: "", tags: "" });
      loadPrompts();
    } catch (err) {
      console.error(err);
      alert("Error (maybe you need to login)");
    }
  };

  const handleBuy = async (id) => {
    try {
      await api.post("/orders/", { prompt_id: id });
      alert("Purchased (mock payment)!");
    } catch (err) {
      console.error(err);
      alert("Error buying (login?)");
    }
  };

  return (
    <div>
      <h2>Prompt Store</h2>

      <h3>Create Prompt</h3>
      <form onSubmit={handleCreate}>
        <input
          name="title"
          placeholder="Title"
          value={form.title}
          onChange={handleChange}
        />
        <textarea
          name="description"
          placeholder="Short description"
          value={form.description}
          onChange={handleChange}
        />
        <textarea
          name="content"
          placeholder="Prompt content"
          value={form.content}
          onChange={handleChange}
        />
        <input
          name="price"
          placeholder="Price"
          value={form.price}
          onChange={handleChange}
        />
        <input
          name="tags"
          placeholder="Tags (comma separated)"
          value={form.tags}
          onChange={handleChange}
        />
        <button type="submit">Publish Prompt</button>
      </form>

      <h3>All Prompts</h3>
      <ul>
        {prompts.map((p) => (
          <li key={p.id}>
            <h4>
              {p.title} – ${p.price}
            </h4>
            <p>{p.description}</p>
            <small>By {p.seller?.username}</small>
            <br />
            <button onClick={() => handleBuy(p.id)}>Buy</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
