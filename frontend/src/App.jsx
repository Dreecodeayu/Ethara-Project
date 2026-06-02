import { useState } from "react";
import "./App.css";

import Products from "./pages/Products";
import Customers from "./pages/Customers";
import Orders from "./pages/Orders";

function App() {
  const [activePage, setActivePage] = useState("dashboard");

  return (
    <div className="container">
      <header className="navbar">
        <div className="logo">
          📦<span>IMS System</span>
        </div>

        <nav>
          <button onClick={() => setActivePage("dashboard")}>
            Dashboard
          </button>

          <button onClick={() => setActivePage("products")}>
            Products
          </button>

          <button onClick={() => setActivePage("customers")}>
            Customers
          </button>

          <button onClick={() => setActivePage("orders")}>
            Orders
          </button>
        </nav>
      </header>

      {activePage === "dashboard" && (
        <>
          <h1>Dashboard</h1>
          <p className="subtitle">
            Inventory & Order Management System Overview
          </p>

          <div className="cards">
            <div className="card">
              <h3>Products</h3>
              <p>Manage inventory items</p>
            </div>

            <div className="card">
              <h3>Customers</h3>
              <p>Manage customer records</p>
            </div>

            <div className="card">
              <h3>Orders</h3>
              <p>Track customer orders</p>
            </div>
          </div>
        </>
      )}

      {activePage === "products" && (
        <div className="section">
          <Products />
        </div>
      )}

      {activePage === "customers" && (
        <div className="section">
          <Customers />
        </div>
      )}

      {activePage === "orders" && (
        <div className="section">
          <Orders />
        </div>
      )}
    </div>
  );
}

export default App;