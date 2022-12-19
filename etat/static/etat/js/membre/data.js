$(document).ready(function(){

// ******************* GESTION AJAX DE LA LISTE DEROULANTE DU SECTEUR D'ACTIVITE *****************************

    var select_typesecteur = $('#typesecteur');
    var select_secteur = $('#secteur');
    var select_activite = $('#activite');

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
                    select_secteur.append("<option value='' selected>--- Sélectionnez un secteur ---</option>");

                    $.each(data.data, function(key, value){
                        select_secteur.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });
            $.ajax({
                url: "/vieprofessionnelle/details-activite", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du niveau scolaire
                    select_activite.html('');
                    select_activite.append("<option value='' selected>--- Sélectionnez un nom ---</option>");

                    $.each(data.data, function(key, value){
                        select_activite.append("<option value='" + value.id + "' >" + value.nom + "</option>");
                    });
                },
            });
        });

// ******************* GESTION DES LISTES DEROULANTES *****************************

    var select_district = $('select[name=select_district]');
    var select_region = $('select[name=select_region]');
    var select_departement = $('select[name=select_departement]');
    var select_ville = $('select[name=select_ville]');
    var select_commune = $('select[name=select_commune]');
    var select_quartier = $('select[name=select_quartier]');
    var select_marche = $('select[name=select_marche]');

        // Traitement AJAX de la region
        $(select_district).change(function(){

            // On utilise ajax pour récupérer les régions
            $.ajax({
                url: "/localisation/details-region", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection de la région
                    select_region.html('');
                    select_region.append("<option value='' selected>--- Selectionnez une région ---</option>");

                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_region.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX du departement
        $(select_region).change(function(){

            // On utilise ajax pour récupérer les départements
            $.ajax({
                url: "/localisation/details-departement", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_departement.html('');
                    select_departement.append("<option value='' selected>--- Selectionnez un département ---</option>");

                    // On initialise la selection du ville
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_departement.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX de la ville
        $(select_departement).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-ville", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_ville.html('');
                    select_ville.append("<option value='' selected>--- Selectionnez une ville ---</option>");

                    // On initialise la selection de la commune
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_ville.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });

        });

        // Traitement AJAX de la commune
        $(select_ville).change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-commune", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du département
                    select_commune.html('');
                    select_commune.append("<option value='' selected>--- Selectionnez une commune ---</option>");

                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_commune.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });

        });

        // Traitement AJAX de la quartier
        select_commune.change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-quartier", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du quartier
                    select_quartier.html('');
                    select_quartier.append("<option value='' selected>--- Selectionnez un quartier ---</option>");

                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_quartier.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

        // Traitement AJAX du marché
        select_quartier.change(function(){

            // On utilise ajax pour récupérer les villes
            $.ajax({
                url: "/localisation/details-marche", // On ajoute l'url absolue en commençant par la racine
                type: 'get',
                data: {
                    id: $(this).val(),
                },
                success: function(data){
                    // On initialise la selection du marché
                    select_marche.html('');
                    select_marche.append("<option value='' selected>--- Selectionnez un marché ---</option>");

                    $.each(data.data, function(key, value){
                        select_marche.append("<option value='" + value.id + "' >" + value.libelle + "</option>");
                    });
                },
            });


        });

// FIN ****************************************************************************

});