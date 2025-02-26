document.addEventListener('keydown', function(event) { 
    if (event.key === 'Enter'){
        window.location.href = "/apps/";
    }
    else if (event.key === 'Backspace'){
        history.back();
    }
    else if (event.key === 'j'){
        window.location.href = "/apps/bio";
    }
}); 