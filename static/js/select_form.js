$(document).ready(function() {

    $('#select-activite-titre').on('change', function() {
        alert('test');
        // var value = $(this).val();
        // var element_main_div = $('#content-form').empty();
    });

    var nr = 1;
    while (nr <= value) {
        var unite = $('<div class="form-group"><label for="unite">Unite Physique</label><input type="text" class="form-control username" id="unite" placeholder="" name="unite" /></div>');
        var quantite = $('<div class="form-group"><label for="quantite">Quantite prevue</label><input type="number" class="form-control" id="quantite" placeholder="" name="quantite" /></div>');
        var periode = $('<div class="form-group"><label for="periode">Periode prevue</label><input type="text" class="form-control" id="periode" placeholder="" name="periode" /></div>');
        var responsable = $('<div class="form-group"><label for="responsable">Responsable d’exécution (projet ou service)</label><input type="text" class="form-control" id="responsable" placeholder="" name="responsable" /></div>');
        var part_etat = $('<div class="form-group"><label for="part">Part Etat Burkina Faso</label><input type="text" class="form-control" id="part" placeholder="" name="part" /></div>');
        var enregistrer = $('<div id="saveBtnContainer" class="text-center mt-4"><button class="btn btn-primary" type="submit">Enregistrer</button></div>');

        element_main_div.append(unite);
        // part_etat.append(enregistrer);

        nr++;
    }
})