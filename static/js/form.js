// -----------------------------------------------------------------------------
function createFormForSelectedOption(selectedOption) {
  // Créer le formulaire HTML
  var formHTML = `
      <div class="form-group">
          <label for="unite">Unité physique</label>
          <input type="text" class="form-control" id="unite" placeholder="" name="unite">
      </div>
      <div class="form-group">
          <label for="quantite">Quantité prévue</label>
          <input type="number" class="form-control" id="quantite" placeholder="" name="quantite">
      </div>
      <div class="form-group">
          <label for="periode">Période prévue</label>
          <input type="text" class="form-control" id="periode" placeholder="" name="periode">
      </div>
      <div class="form-group">
          <label for="responsable">Responsable d’exécution (projet ou service)</label>
          <input type="text" class="form-control" id="responsable" placeholder="" name="responsable">
      </div>
      <div class="form-group">
          <label for="part">Part Etat Burkina Faso</label>
          <input type="text" class="form-control" id="part" placeholder="" name="part">
      </div>
      <div id="saveBtnContainer" class="text-center mt-4">
          <button class="btn btn-primary" type="submit">Enregistrer</button>
      </div>
  `;

  // Ajouter le formulaire au conteneur
  document.getElementById("content-form").innerHTML = formHTML;
  // Ajouter une classe pour appliquer un effet de transition
  document.getElementById("content-form").classList.add("fade-in");
}

// Écouter le changement de sélection dans le <select>
document.getElementById("activiteSelect").addEventListener("change", function () {
  console.log('test change success')
  var selectedOption = this.value;

  // Appeler la fonction pour créer le formulaire correspondant à l'option sélectionnée
  createFormForSelectedOption(selectedOption);
  console.log('success');
});