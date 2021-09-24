function genQrCode(el){
    let link = el.previousElementSibling.href;
    let fname = el.previousElementSibling.textContent;

    let qrContainer = document.getElementById('qrContainer');
    qrContainer.innerHTML =""
    qrContainer.innerHTML =link+"<hr>";

    new QRCode(qrContainer, link);

                    async function postData(url, data ) {
                // Default options are marked with *
                    const response = await fetch(url, {
                    method: 'POST', // *GET, POST, PUT, DELETE, etc.
                    mode: 'cors', // no-cors, *cors, same-origin
                    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
                    credentials: 'same-origin', // include, *same-origin, omit
                   
                    headers : { 
                        'Content-Type': 'application/json',
                        // 'Accept': 'application/json'
                       },
                   
                    redirect: 'follow', // manual, *follow, error
                    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
                    body: JSON.stringify(data) // body data type must match "Content-Type" header
                });
                return response; // parses JSON response into native JavaScript objects
                }

                postData('/gen', { link: link , fname: fname})
                .then(data => {
                    console.log(data); // JSON data parsed by `data.json()` call
                });
}