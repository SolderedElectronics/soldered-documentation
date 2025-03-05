import React from "react";
import styles from "./ProductTable.module.css";

const ProductTable = ({ products }) => {
  return (
    <div className={styles.tableContainer}>
      <table className={styles.customTable}>
        <colgroup>
          <col style={{ width: "15%" }} />
          <col style={{ width: "40%" }} />
          <col style={{ width: "20%" }} />
          <col style={{ width: "25%" }} />
        </colgroup>
        <thead>
          <tr>
            <th>SKU</th>
            <th>Product Name</th>
            <th>Store Link</th>
            <th>Solde.red Page</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product, index) => (
            <tr key={index}>
              <td>{product.sku}</td>
              <td>{product.name}</td>
              <td>
                <a
                  href={product.storeLink}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  View on Soldered.com
                </a>
              </td>
              <td>
                <a
                  href={product.soldeRedLink}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  View on solde.red
                </a>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductTable;
