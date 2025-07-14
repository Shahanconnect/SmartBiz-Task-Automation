document.addEventListener("DOMContentLoaded", function () {
    const addItemBtn = document.getElementById("addItem");
    const itemTable = document.getElementById("itemTable").querySelector("tbody");
    const invoiceTotal = document.getElementById("invoiceTotal");
    const generatePDFBtn = document.getElementById("generatePDF");
  
    // 🧮 Calculate total for a row
    function updateRowTotal(row) {
      const qty = parseFloat(row.querySelector(".qty").value) || 0;
      const price = parseFloat(row.querySelector(".price").value) || 0;
      const total = qty * price;
      row.querySelector(".itemTotal").textContent = total.toFixed(2);
      updateInvoiceTotal();
    }
  
    // 💰 Update invoice grand total
    function updateInvoiceTotal() {
      let total = 0;
      document.querySelectorAll(".itemTotal").forEach(el => {
        total += parseFloat(el.textContent) || 0;
      });
      invoiceTotal.textContent = total.toFixed(2);
    }
  
    // ➕ Add new item row
    addItemBtn.addEventListener("click", () => {
      const newRow = document.querySelector(".itemRow").cloneNode(true);
      newRow.querySelectorAll("input").forEach(input => input.value = "");
      newRow.querySelector(".itemTotal").textContent = "0.00";
      itemTable.appendChild(newRow);
      const firstInput = newRow.querySelector("input");
      if (firstInput) firstInput.focus();
    });
  
    // ♻️ Update totals when qty or price change
    itemTable.addEventListener("input", function (e) {
      if (e.target.classList.contains("qty") || e.target.classList.contains("price")) {
        const row = e.target.closest(".itemRow");
        updateRowTotal(row);
      }
    });
  
    // ❌ Remove item row
    itemTable.addEventListener("click", function (e) {
      if (e.target.classList.contains("removeItem")) {
        const rows = itemTable.querySelectorAll(".itemRow");
        if (rows.length > 1) {
          e.target.closest(".itemRow").remove();
          updateInvoiceTotal();
        } else {
          alert("At least one item must remain in the invoice.");
        }
      }
    });
  
    // 📄 Generate PDF
    generatePDFBtn.addEventListener("click", function () {
      const element = document.getElementById("invoiceForm");
      const totalAmount = parseFloat(invoiceTotal.textContent) || 0;
      
      if (totalAmount === 0) {
        alert("Invoice is empty. Please add items before generating a PDF.");
        return;
      }
  
      html2pdf()
        .set({
          margin: 10,
          filename: "invoice.pdf",
          image: { type: "jpeg", quality: 0.98 },
          html2canvas: { scale: 2 },
          jsPDF: { unit: "mm", format: "a4", orientation: "portrait" }
        })
        .from(element)
        .save();
    });
  
  });
  