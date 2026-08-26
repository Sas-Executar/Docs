from .registry import load_folder_registry, load_skill_index

DOMAIN_DESTINATIONS = {
    'business': '10-business',
    'product-management': '20-produtos',
    'marketing': '30-editorial-marketing',
    'sales': '40-comercial-servicos',
    'data': '60-dados',
    'operations': '70-operacao-governanca',
    'engineering': '80-tecnologia-plataformas',
    'design': '90-assets-compartilhados',
}

def folder_by_id(folder_id):
    for row in load_folder_registry():
        if row['folder_id'] == folder_id:
            return row
    return None

def skills_for_plugin(plugin_id):
    return [s for s in load_skill_index().get('skills', []) if s.get('plugin_id') == plugin_id]
