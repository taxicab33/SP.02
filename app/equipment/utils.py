class EquipmentMixin():
    @staticmethod
    def get_equipment_extra_context_data(context: dict):
        """Получаем все дополнительные данные связанные с оборудованием"""
        equipment = context['equipment_object']
        context['title'] = equipment
        context['expendable_materials'] = equipment.get_expendable_materials()
        context['networks_settings'] = equipment.get_network_settings()
        context['inventory'] = equipment.get_inventory()
        context['classrooms_history'] = equipment.get_classrooms_history()
        context['resp_users_history'] = equipment.get_resp_users_history()
        context['programs'] = equipment.get_programs()
        return context