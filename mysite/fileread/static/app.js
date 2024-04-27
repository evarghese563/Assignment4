function submitFile(){
    const item = document.getElementById("item")
    const [file] = document.getElementById("inputfile").files
    const reader = new FileReader();


    reader.addEventListener(
        "load",
        () => {
            // this will then display a text file
            item.innerText = reader.result;
            const value = item.innerText
            cartValue(value)

            localStorage.setItem("item",item.innerText);
        },
        false,
    );

    if (file) {
        reader.readAsText(file);
    }

    
}

function cartValue (value){
    let content = document.getElementById("checkout")
    let num = value.length
    content.innerText = "Checkout : " + num

}

