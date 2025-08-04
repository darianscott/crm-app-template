import { sendReportPayload } from "./send_payload";
import { askHowToSort } from "./sort";

async function buildPayload(resource) {
  const form = document.getElementById(form);
  const fields = {};
  const filters = {};
  const  inputOptions = {};


  form.querySelectorAll('input').forEach(el => {
        // Skip disabled or empty fields
        if (el.type === 'checkbox' && el.checked) {
          if (el.name) {
            fields[el.name] = true;
          }
          if (el.dataset.filters) {
            filters[el.dataset.filters];
            inputOptions[el.dataset.filters] = el.closest('label').textContent.trim();   
          }            
        }
    });

    // Validate: Make sure we have at least one field to send
    if (Object.keys(fields).length === 0) {
        console.error('No fields provided for payload.');
        alert('Please fill out at least one field before submitting.');
        return;
    }
    
    const sort = await askHowToSort(inputOptions)

    // Build payload
    const payload = {
      resource,
      fields: fields,
      filters:filters,
      joins: false,
      sort_by: sort,
      format: 'csv',
      page: 1,
      per_page: 30,
    }

    await sendReportPayload();










}