import React from "react";
import styles from "./functionDocumentation.module.css";

const FunctionDocumentation = ({ functionName, description, returnDescription, returnType, parameters }) => (
  <div className={styles.functionDocumentation}>
    {/* Header Section */}
    <div className={styles.headerSection}>
      <h3>{functionName}</h3>
    </div>

    {/* Divider Line */}
    <div className={styles.headerDivider}></div>

    {/* Body Section */}
    <div className={styles.bodySection}>
      {/* Description */}
      <p>{description}</p>

      {/* Return Type and Description */}
      {(returnType || returnDescription) && (
        <div className={styles.returnSection}>
          {returnType && (
            <p>
              <strong>Returns type:</strong> <code>{returnType}</code>
            </p>
          )}
          {returnDescription && (
            <p>
              <strong>Returns value:</strong> {returnDescription}
            </p>
          )}
        </div>
      )}

      {/* Parameters Table (Only Render if Parameters Exist) */}
      {parameters && parameters.length > 0 && (
        <>
          <p className={styles.paramsText}>Function parameters:</p>
          <table>
            <thead>
              <tr>
                <th>Type</th>
                <th>Name</th>
                <th>Description</th>
              </tr>
            </thead>
            <tbody>
              {parameters.map((param, index) => (
                <tr key={index}>
                  <td><code>{param.type}</code></td>
                  <td><code>{param.name}</code></td>
                  <td>{param.description}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  </div>
);

export default FunctionDocumentation;
