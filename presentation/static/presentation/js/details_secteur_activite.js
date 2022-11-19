$(document).ready(function(){

// ******************* GESTION AJAX DE L'AJOUT D'UNE COOPERATIVE *****************************

    var select_typesecteur = $('#select_typesecteur');
    var select_secteur = $('#select_secteur');

    // Traitement AJAX du niveau
    select_typesecteur.change(function(){
            // On utilise ajax pour récupérer les niveaux
            $.ajax({
                url: "/vieprofessionnelle/details-secteur", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    select_secteur.html('');
                    select_secteur.append("<option value='' selected>--- Sélectionnez un secteur d'activité ---</option>");

                    $.each(data.data, function(key, value){
                        select_secteur.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });
        });

// ******************* GESTION DE L'AJOUT D'UN SECTEUR D'ACTIVITE *****************************

    var envoyer_secteur = $('#envoyer_secteur');
    var select_typesecteur = $('#select_typesecteur');
    var select_secteur = $('#select_secteur');
    var id_membre_secteur = $('#id_membre_secteur');
    var tablesecteur = $('#tablesecteur tbody');
    var valider = true;


    // Traitement AJAX
    envoyer_secteur.click(function(e){
        e.preventDefault(); // On annule l'envoi du formulaire

        if(!select_typesecteur.val()){
            valider = false;
            alert('Veuillez sélectionner le type de secteur.');
            select_typesecteur.focus();
        }else if(!select_secteur.val()){
            valider = false;
            alert("Veuillez sélectionner le secteur d'activité.");
            select_secteur.focus();
        }else{
            valider = true;
        }

        if(valider){
            // On utilise ajax pour transmetre les données
            $.ajax({
                url: "/presentation/ajouter-secteur-membre", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id_membre_secteur: id_membre_secteur.val(),
                    select_secteur: select_secteur.val(),
                },
                success: function(data){

                    // On vide le contenu
                    tablesecteur.html('');

                    // On remplit les champs
                    $.each(data.data, function(k, valeur){
                        k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                        tablesecteur.append(`

                            <tr>
                                <td>` + k + `</td>
                                <td>` + valeur.typesecteur + `</td>
                                <td>` + valeur.secteur + `</td>
                                <td class='text-center'>
                                    <button type='button' title='Supprimer' class='btn btn-outline-danger btn-sm' data-toggle='modal' data-target='#secteursupprimermodal` + valeur.id + `' data-backdrop='static'><i class='fas fa-trash-alt'></i></button>
                                    <!-- Modal -->
                                    <div class='modal fade' id='secteursupprimermodal` + valeur.id + `' role='dialog'>
                                        <div class='modal-dialog'>

                                            <!-- Modal content-->
                                            <div class='modal-content'>
                                                <div class='modal-header'>
                                                    <h4 class='modal-title'>Confirmez-vous la suppression ?</h4>
                                                    <button type='button' class='close' data-dismiss='modal'>&times;</button>
                                                </div>
                                                <div class='modal-body'>
                                                    <h5>
                                                        Secteur : <strong>` + valeur.secteur + `</strong>
                                                    </h5>
                                                </div>
                                                <div class='modal-footer justify-content-center'>

                                                    <form style='display:inline-block; text-align:center' method='get' action='#'>
                                                        <input type='text' name='id_membre_secteur_s' id='id_membre_secteur_s` + valeur.id + `' value='` + valeur.id_membre + `' hidden>
                                                        <button type='submit' name='supprimer_s' value='` + valeur.id + `' class='btn btn-success btn-sm'>Oui</button>
                                                    </form>
                                                    <button class='btn btn-danger btn-sm' name='annuler_s' data-dismiss='modal'>Non</button>

                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                    <!-- Modal Fin -->
                                </td>
                            </tr>

                        `);
                    });

                    supprimer_ligne_secteur(); // On appelle la fonction pour prendre en compte les nouvelles données
                },
                statusCode: {
                    404: function(data){
                            alert('Veuillez réessayer car une erreur est survenue.');
                         },
                },
            });
        }

    });


// ******************* GESTION DE LA SUPPRESSION D'UN SECTEUR D'ACTIVITE *****************************
    function supprimer_ligne_secteur(){
        var supprimer_s = $('button[name=supprimer_s]');
        var annuler_s = $('button[name=annuler_s]');

        // Traitement AJAX
        supprimer_s.each(function(){
            $(this).click(function(e){
                e.preventDefault();

                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/presentation/supprimer-secteur-membre", // On ajoute l'url absolue en commençant par la racine
                    type: 'get',
                    data: {
                        id_membre_secteur_s: $('#id_membre_secteur_s'+$(this).val()).val(),
                        supprimer_s: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tablesecteur.html('');

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tablesecteur.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typesecteur + `</td>
                                    <td>` + valeur.secteur + `</td>
                                    <td class='text-center'>
                                        <button type='button' title='Supprimer' class='btn btn-outline-danger btn-sm' data-toggle='modal' data-target='#secteursupprimermodal` + valeur.id + `' data-backdrop='static'><i class='fas fa-trash-alt'></i></button>
                                        <!-- Modal -->
                                        <div class='modal fade' id='secteursupprimermodal` + valeur.id + `' role='dialog'>
                                            <div class='modal-dialog'>

                                                <!-- Modal content-->
                                                <div class='modal-content'>
                                                    <div class='modal-header'>
                                                        <h4 class='modal-title'>Confirmez-vous la suppression ?</h4>
                                                        <button type='button' class='close' data-dismiss='modal'>&times;</button>
                                                    </div>
                                                    <div class='modal-body'>
                                                        <h5>
                                                            Secteur : <strong>` + valeur.secteur + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class='modal-footer justify-content-center'>

                                                        <form style='display:inline-block; text-align:center' method='get' action='#'>
                                                            <input type='text' name='id_membre_secteur_s' id='id_membre_secteur_s` + valeur.id + `' value='` + valeur.id_membre + `' hidden>
                                                            <button type='submit' name='supprimer_s' value='` + valeur.id + `' class='btn btn-success btn-sm'>Oui</button>
                                                        </form>
                                                        <button class='btn btn-danger btn-sm' name='annuler_s' data-dismiss='modal'>Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);

                        });

                        annuler_s.trigger('click');
                        supprimer_ligne_secteur();
                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez réessayer car une erreur est survenue.');
                             },
                    },
                });

            });
        });
    }

    supprimer_ligne_secteur();




// ****************************************************************************

});