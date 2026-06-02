function Dashboard({ products, customers, orders }) {
  return (
    <div>
      <h2>Dashboard</h2>

      <div className="cards">
        <div className="card">
          <h3>Total Products</h3>
          <p>{products.length}</p>
        </div>

        <div className="card">
          <h3>Total Customers</h3>
          <p>{customers.length}</p>
        </div>

        <div className="card">
          <h3>Total Orders</h3>
          <p>{orders.length}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;