import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from collections import OrderedDict
import json


# import ckanext.knowtest.cli as cli
# import ckanext.knowtest.helpers as helpers
import ckanext.knowtest.views as views
from ckanext.knowtest.logic import (
    validators#     action, auth, validators
)


class KnowTestPlugin(plugins.SingletonPlugin):
    # If only needs compatibility for CKAN 2.11 + you can define the classes directly above
    plugins.implements(plugins.IConfigurer)

    # plugins.implements(plugins.IAuthFunctions)
    # plugins.implements(plugins.IActions)
    plugins.implements(plugins.IBlueprint)
    # plugins.implements(plugins.IClick)
    # plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.IFacets)
    plugins.implements(plugins.IPackageController)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "knowtest")


    # IAuthFunctions

    # def get_auth_functions(self):
    #     return auth.get_auth_functions()

    # IActions

    # def get_actions(self):
    #     return action.get_actions()

    # IBlueprint

    def get_blueprint(self):
        return views.get_blueprints()

    # IClick

    # def get_commands(self):
    #     return cli.get_commands()

    # ITemplateHelpers

    # def get_helpers(self):
    #     return helpers.get_helpers()

    # IValidators

    def get_validators(self):
        return validators.get_validators()

    # IFacets

    def dataset_facets(self, facets_dict, package_type):
        """Modify the facets_dict and return it
        """
        new_facets = OrderedDict()
        new_facets['type'] = toolkit._('Digitization Resource Type')
        new_facets['task_cluster'] = toolkit._('Task Clusters')

        # Add the rest of the facets
        for key, value in facets_dict.items():
            new_facets[key] = value

        return new_facets
    
    def group_facets(self, facets_dict, group_type, package_type):
        return facets_dict
    
    def organization_facets(self, facets_dict, organization_type, package_type):
        return facets_dict

    def before_dataset_index(self, pkg_dict):
        # Get the task_cluster value
        task_cluster = pkg_dict.get('task_cluster', '')
        print(f"Incoming task_cluster: {task_cluster} of type {type(task_cluster)}")
        
        try:
            # If it's a JSON string, parse it
            if isinstance(task_cluster, str) and task_cluster.strip().startswith('['):
                task_clusters = json.loads(task_cluster)
            # If it's already a list, use it as is
            elif isinstance(task_cluster, list):
                task_clusters = task_cluster
            else:
                task_clusters = []

            # Ensure all items are strings and remove empty values
            task_clusters = [str(t).strip() for t in task_clusters if t]
            
            print(f"Processed task_clusters: {task_clusters}")
            pkg_dict['task_cluster'] = task_clusters
            
        except json.JSONDecodeError:
            # Handle invalid JSON
            print(f"Error parsing task_cluster JSON: {task_cluster}")
            pkg_dict['task_cluster'] = []
        
        return pkg_dict
   
    # Required methods with default implementations
    
    def before_dataset_search(self, search_params):
        return search_params

    def after_dataset_search(self, search_results, search_params):
        return search_results

    def before_dataset_view(self, pkg_dict):
        return pkg_dict

    def after_dataset_create(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_update(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_delete(self, context, pkg_dict):
        return pkg_dict

    def after_dataset_show(self, context, pkg_dict):
        return pkg_dict

    def create(self, entity):
        pass

    def edit(self, entity):
        pass

    def delete(self, entity):
        pass

    def read(self, entity):
        pass