$(document).ready(function() {

// Ajout du champ du champ de recherche ************************
    var table_recherche_parent = "table_recherche_parent";
    var table = $('#' + table_recherche_parent ).DataTable( {

    // Pagination du tableau
    // Paramètres optionnels du DATATABLES
    paging: true,
    pageLength: 10,
    lengthChange: true,
    autoWidth: true,
    searching : true,
    bInfo : true,
    bSort : true,
    select : true,
    order : [],

    // Gestion de l'affichage de la langue des champs
        language: {
        processing:     "Traitement en cours...",
        search:         "Rechercher&nbsp;:",
        lengthMenu:    "Afficher _MENU_ &eacute;l&eacute;ments",
        info:           "Affichage de l'&eacute;lement _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
        infoEmpty:      "Affichage de l'&eacute;lement 0 &agrave; 0 sur 0 &eacute;l&eacute;ments",
        infoFiltered:   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
        infoPostFix:    "",
        loadingRecords: "Chargement en cours...",
        zeroRecords:    "Aucun &eacute;l&eacute;ment &agrave; afficher",
        emptyTable:     "Aucune donnée disponible dans le tableau",
        paginate: {
            first:      "Premier",
            previous:   "Pr&eacute;c&eacute;dent",
            next:       "Suivant",
            last:       "Dernier"
        },
        aria: {
            sortAscending:  ": activer pour trier la colonne par ordre croissant",
            sortDescending: ": activer pour trier la colonne par ordre décroissant"
        }
    },

    } );

    // Recherche globale du tableau
    var monTableau = $('#'+ table_recherche_parent).DataTable(); // On récupère le tableau
    $('#recherche_parent').keyup(function(){
        monTableau.search($(this).val()).draw();
    });
// Fin de recherche **************************************************


// ******************* GESTION DES AFFICHAGES DES CHAMPS POUR AJOUTER UN PARENT *****************************

    var btn_p_ajouter = $('#btn_p_ajouter');
    var btn_p_annuler = $('#btn_p_annuler');
    var select_typeparent = $('#select_typeparent');
    var nomprenoms = $('input[name=nomprenoms]');
    var datenaissance = $('input[name=datenaissance]');
    var contact = $('input[name=contact]');
    var adresse = $('input[name=adresse]');
    var id_membre_parent = $('#id_membre_parent');
    var tableparent = $('#tableparent tbody');
    var trouver = true;

    // Traitement AJAX
    btn_p_ajouter.click(function(e){
            e.preventDefault(); // On annule l'envoi du formulaire

            if(!select_typeparent.val()){
                trouver = false;
                alert('Veuillez sélectionner le type de parent.');
                select_typeparent.focus();
            }else if(!nomprenoms.val()){
                trouver = false;
                alert('Veuillez renseigner le nom et prénoms.');
                nomprenoms.focus();
            }else if(!datenaissance.val()){
                trouver = false;
                alert('Veuillez renseigner la date de naissance.');
                datenaissance.focus();
            }else{
                trouver = true;
            }

            if(trouver){
                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/vieprofessionnelle/ajouter-parent", // On ajoute l'url absolue en commençant par la racine
                    type: 'POST',
                    data: {
                        id_json: $('#id_json').val(),
                        id_membre_parent: id_membre_parent.val(),
                        select_typeparent: select_typeparent.val(),
                        nomprenoms: nomprenoms.val(),
                        datenaissance: datenaissance.val(),
                        adresse: adresse.val(),
                        contact: contact.val(),
                        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tableparent.html("");

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tableparent.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typeparent + `</td>
                                    <td>` + valeur.nomprenoms + `</td>
                                    <td>` + valeur.datenaissance + `</td>
                                    <td>` + valeur.adresse + `</td>
                                    <td>` + valeur.contact + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#parentsupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="parentsupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Parent : <strong>` + valeur.nomprenoms + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <input type="text" name="id_membre_parent_s" id="id_membre_parent_s` + valeur.id + `" value="` + valeur.id_membre + `" hidden>
                                                            <button type="submit" name="supprimer_p" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_p" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);
                        });

                        // Gestion des fermetures des boutons
                        btn_p_annuler.trigger('click'); // On initialise les champs

                        supprimer_ligne_parent(); // On appelle la fonction pour prendre en compte les nouvelles données

                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez renseigner les champs SVP.');
                             },
                    },
                });
            }



        });

// ******************* GESTION DE LA SUPPRESSION D'UN PARENT *****************************
    function supprimer_ligne_parent(){
        var supprimer_p = $('button[name=supprimer_p]');
        var annuler_p = $('button[name=annuler_p]');

        // Traitement AJAX
        supprimer_p.each(function(){
            $(this).click(function(e){
                e.preventDefault();

                // On utilise ajax pour transmetre les données
                $.ajax({
                    url: "/presentation/supprimer-parent-membre", // On ajoute l'url absolue en commençant par la racine
                    type: 'get',
                    data: {
                        id_membre_parent_s: $('#id_membre_parent_s'+$(this).val()).val(),
                        supprimer_p: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tableparent.html('');

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tableparent.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typeparent + `</td>
                                    <td>` + valeur.nomprenoms + `</td>
                                    <td>` + valeur.datenaissance + `</td>
                                    <td>` + valeur.adresse + `</td>
                                    <td>` + valeur.contact + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#parentsupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="parentsupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Parent : <strong>` + valeur.nomprenoms + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <input type="text" name="id_membre_parent_s" id="id_membre_parent_s` + valeur.id + `" value="` + valeur.id_membre + `" hidden>
                                                            <button type="submit" name="supprimer_p" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_p" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);

                        });

                        annuler_p.trigger('click');
                        supprimer_ligne_parent();
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

    supprimer_ligne_parent(); // On appelle la fonction

// ******************* GESTION DE L'AJOUT D'UN PARENT A PARTIR DU TABLEAU DE RECHERCHE ***

var liste_btn_ajouter = $('#table_recherche_parent tbody button');

    liste_btn_ajouter.each(function(){

        $(this).click(function(e){
            e.preventDefault();

            // On utilise ajax pour transmetre les données
            $.ajax({
                    url: "/presentation/ajouter-parent-membre", // On ajoute l'url absolue en commençant par la racine
                    type: 'GET',
                    data: {
                        id_membre_parent: id_membre_parent.val(),
                        parent: $(this).val(),
                    },
                    success: function(data){

                        // On vide le contenu
                        tableparent.html("");

                        // On remplit les champs
                        $.each(data.data, function(k, valeur){
                            k++; // On incrémente la variable à chaque fois pour avoir le nombre exacte car la variable débute par 0
                            tableparent.append(`

                                <tr>
                                    <td>` + k + `</td>
                                    <td>` + valeur.typeparent + `</td>
                                    <td>` + valeur.nomprenoms + `</td>
                                    <td>` + valeur.datenaissance + `</td>
                                    <td>` + valeur.adresse + `</td>
                                    <td>` + valeur.contact + `</td>
                                    <td class="text-center">
                                        <button type="button" title="Supprimer" class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#parentsupprimermodal` + valeur.id + `" data-backdrop="static"><i class="fas fa-trash-alt"></i></button>
                                        <!-- Modal -->
                                        <div class="modal fade" id="parentsupprimermodal` + valeur.id + `" role="dialog">
                                            <div class="modal-dialog">

                                                <!-- Modal content-->
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <h4 class="modal-title">Confirmez-vous la suppression ?</h4>
                                                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                                                    </div>
                                                    <div class="modal-body">
                                                        <h5>
                                                            Parent : <strong>` + valeur.nomprenoms + `</strong>
                                                        </h5>
                                                    </div>
                                                    <div class="modal-footer justify-content-center">

                                                        <form style="display:inline-block; text-align:center" method="get" action="#">
                                                            <input type="text" name="id_membre_parent_s" id="id_membre_parent_s` + valeur.id + `" value="` + valeur.id_membre + `" hidden>
                                                            <button type="submit" name="supprimer_p" value="` + valeur.id + `" class="btn btn-success btn-sm">Oui</button>
                                                        </form>
                                                        <button class="btn btn-danger btn-sm" name="annuler_p" data-dismiss="modal">Non</button>

                                                    </div>
                                                </div>

                                            </div>
                                        </div>
                                        <!-- Modal Fin -->
                                    </td>
                                </tr>

                            `);
                        });

                        supprimer_ligne_parent(); // On appelle la fonction pour prendre en compte les nouvelles données

                    },
                    statusCode: {
                        404: function(data){
                                alert('Veuillez renseigner les champs SVP.');
                             },
                    },
                });
        });

    });


// *****************************************************************************

} );