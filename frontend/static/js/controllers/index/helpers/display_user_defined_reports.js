export function displayReport(data, targetSelector) {
    const container = document.querySelector(targetSelector);
    if (!container) return;
  
    if (!data || !data.data || data.data.length === 0) {
        container.innerHTML = "<p>No data available.</p>";
        return;
    }

    const { fields, data: rows } = data;

    // Build table
    const table = document.createElement("table");
    table.classList.add("report-table");

    // Header row
    const thead = document.createElement("thead");
    const headerRow = document.createElement("tr");
    fields.forEach(field => {
        const th = document.createElement("th");
        th.textContent = field.replace(/_/g, " ").toUpperCase();
        headerRow.appendChild(th);
    });
    thead.appendChild(headerRow);
    table.appendChild(thead);

    // Data rows
    const tbody = document.createElement("tbody");
    rows.forEach(row => {
        const tr = document.createElement("tr");
        fields.forEach(field => {
            const td = document.createElement("td");
            td.textContent = row[field] ?? "";
            tr.appendChild(td);
        });
        tbody.appendChild(tr);
    });
    table.appendChild(tbody);

    // Insert table
    container.innerHTML = "";
    container.appendChild(table);
}
