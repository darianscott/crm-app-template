export async function askHowToSort(inputOptions) {
    
    Swal.fire({
        title: "How would you like to your report sorted?",
        input: "radio",
        inputOptions,
        showCancelButton: true,
        cancelButtonText: "Skip",
        inputValidatior: (value) => {
            if (!value) {
                return 'Please make a selection';
            }
        },
    
    }), await result
            return result    
};