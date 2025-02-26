document.addEventListener('keydown', function(event) { 
    if (event.key === 'Backspace'){
        window.location.href = "/apps";
    }
    else if (event.key === '1'){
        window.location.href = "/apps/payments";
    }
    else if (event.key === '2'){
        window.location.href = "/apps/study";
    }
    else if (event.key === '3'){
        window.location.href = "/apps/e_wallet";
    }
    else if (event.key === 'Home'){
        window.location.href = "/";
    }
    else if (event.key === 'j'){
        window.location.href = "/apps/bio";
    }
}); 