export function askSort()  {
    Swal.fire({
    title: "Sort Results?",
    input: "text",
    inputLabel: "Enter a field to sort by (e.g. user.last_name)",
    showCancelButton: true,
    confirmButtonText: "Sort",
    cancelButtonText: "Skip"
    }).then(sortResult => {
        if (sortResult.value) {
            payload.sort_by = sortResult.value;
        }

        console.log("Final Payload:", payload);
        showJSONPreview(payload); // or send to backend
    });
};