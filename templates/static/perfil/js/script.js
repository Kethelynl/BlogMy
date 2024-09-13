document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const query = document.querySelector('input[name="q"]').value;

    fetch(`/topicos/?q=${query}`)
      .then(response => response.text())
      .then(html => {
        document.querySelector('#results').innerHTML = html;  // Substitui a lista atual pelos resultados
      });
});

