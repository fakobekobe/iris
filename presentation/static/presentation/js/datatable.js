$(document).ready(function(){

// ******************* GESTION DES LISTES DEROULANTES *****************************

    var niveau = $('select[name=niveau]');
    var niveauscolaire = $('select[name=niveauscolaire]');

    // Traitement AJAX du niveau
    niveau.change(function(){

            // On utilise ajax pour récupérer les niveaux
            $.ajax({
                url: "/presentation/details-niveauscolaire", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    niveauscolaire.html('');
                    niveauscolaire.append("<option value='' selected>--- Selectionnez un niveau scolaire ---</option>");

                    $.each(data.data, function(key, value){
                        niveauscolaire.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });


// ******************* FIN DE LA GESTION DES LISTES DEROULANTES *****************************

});