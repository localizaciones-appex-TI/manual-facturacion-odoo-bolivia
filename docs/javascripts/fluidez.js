// Las capturas aparecen con un fundido al terminar de cargar.
// La clase "fundido" en <html> activa el efecto solo si este script corre: sin él, las imágenes se ven normal.
document.documentElement.classList.add("fundido");

function marcarImagenes() {
  document.querySelectorAll(".md-typeset img").forEach(function (img) {
    if (img.complete && img.naturalWidth > 0) {
      img.classList.add("cargada");
    } else {
      var listo = function () { img.classList.add("cargada"); };
      img.addEventListener("load", listo, { once: true });
      img.addEventListener("error", listo, { once: true });
    }
  });
}

// Material for MkDocs cambia de página sin recargar (navegación instantánea): document$ avisa cada cambio.
if (typeof document$ !== "undefined") {
  document$.subscribe(marcarImagenes);
} else {
  document.addEventListener("DOMContentLoaded", marcarImagenes);
}
