define(['application', 'tpl!./templates/logs.tpl'], function (App, template) {
    App.module('Monitor.Views', function (Views, App, Backbone, Marionette, $, _) {
        Views.Logs = Marionette.ItemView.extend({
            template: template
        });
    });

    return App.module('Monitor.Views').Logs;
});
