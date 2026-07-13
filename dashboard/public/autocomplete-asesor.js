// Script de autocomplete mejorado para buscar asesores

function mostrarTodasLasSugerencias() {
    const sugerencias = document.getElementById('asesorSugerencias');
    if (!sugerencias) return;
    
    sugerencias.innerHTML = '';
    
    const asesoresLista = window.asesoresLista || [];
    asesoresLista.forEach(asesor => {
        const div = document.createElement('div');
        div.textContent = asesor;
        div.style.padding = '8px 12px';
        div.style.cursor = 'pointer';
        div.style.borderBottom = '1px solid #eee';
        div.style.fontSize = '12px';
        div.onmouseover = () => div.style.background = '#f0f0f0';
        div.onmouseout = () => div.style.background = 'white';
        div.onclick = () => {
            document.getElementById('asesorFilter').value = asesor;
            sugerencias.style.display = 'none';
            actualizarDatos();
        };
        sugerencias.appendChild(div);
    });
    
    if (asesoresLista.length > 0) {
        sugerencias.style.display = 'block';
    }
}

function filtrarAsesor() {
    const input = document.getElementById('asesorFilter');
    const sugerencias = document.getElementById('asesorSugerencias');
    const valor = input.value.toLowerCase().trim();
    const asesoresLista = window.asesoresLista || [];

    // Si está vacío, mostrar todos
    if (valor === '') {
        mostrarTodasLasSugerencias();
        return;
    }

    // Filtrar asesores que coincidan (case-insensitive)
    const coincidencias = asesoresLista.filter(a => 
        a.toLowerCase().includes(valor)
    ).slice(0, 20);  // Mostrar máximo 20

    sugerencias.innerHTML = '';
    
    if (coincidencias.length === 0) {
        const div = document.createElement('div');
        div.textContent = 'No encontrado';
        div.style.padding = '10px 12px';
        div.style.color = '#999';
        div.style.fontSize = '12px';
        sugerencias.appendChild(div);
        sugerencias.style.display = 'block';
        return;
    }

    coincidencias.forEach(asesor => {
        const div = document.createElement('div');
        div.textContent = asesor;
        div.style.padding = '8px 12px';
        div.style.cursor = 'pointer';
        div.style.borderBottom = '1px solid #eee';
        div.style.fontSize = '12px';
        div.onmouseover = () => div.style.background = '#f0f0f0';
        div.onmouseout = () => div.style.background = 'white';
        div.onclick = () => {
            input.value = asesor;
            sugerencias.style.display = 'none';
            actualizarDatos();
        };
        sugerencias.appendChild(div);
    });

    sugerencias.style.display = 'block';
}

// Initialize autocomplete after page loads
document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('asesorFilter');
    const sugerencias = document.getElementById('asesorSugerencias');
    
    if (input && sugerencias) {
        input.addEventListener('focus', function() {
            if (this.value === '') {
                mostrarTodasLasSugerencias();
            }
        });
    }
});

// Cerrar sugerencias al hacer click fuera
document.addEventListener('click', function(e) {
    const input = document.getElementById('asesorFilter');
    const sugerencias = document.getElementById('asesorSugerencias');
    
    if (input && sugerencias && !input.contains(e.target) && !sugerencias.contains(e.target)) {
        sugerencias.style.display = 'none';
    }
});
