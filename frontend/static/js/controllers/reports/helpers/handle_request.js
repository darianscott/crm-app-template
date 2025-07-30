import { askJoins } from "./ask_joins";
import { askSort } from "./sort";


export async function handleSubmit() {
    const resources = buildResources();
    const models = Object.keys(resources);


    if (models.length === 0) {
        Swal.fire("No fields selected", "Please select at least one field.", "warning");
        return;
    }

    let payload = {
        resources,
        join: false,
        sort_by: null,
        format: "csv"
    };

    if (models.length > 1) {
        joins = await askJoins()
        askSortAndFormat();
    } 
    askSortAndFormat();
}

