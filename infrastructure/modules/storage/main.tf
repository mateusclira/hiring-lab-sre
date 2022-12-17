
resource "azurerm_storage_account" "main" {
  name                     = "st${var.unique_person_name}"
  resource_group_name      = var.rg_name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
