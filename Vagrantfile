# -*- mde: ruby -*-
# vi: set ft=ruby :
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

Vagrant.configure("2") do |config|
    # Tipo de máquina.
    config.vm.box = "google/gce"

    #config.ssh.private_key_path = '~/.ssh/id_rsa'

    config.vm.provider :google do |google, override|
        # ID del proyecto.
        #google.google_project_id = ENV['ID_GCP']
        google.google_project_id ="projectz"

        # Email del cliente de google.
        #google.google_client_email = ENV['CEM']
        google.google_client_email = "iv-524@projectz.iam.gserviceaccount.com"

        # JSON con información de la cuenta de Google Cloud, proyecto y demás.
        #google.google_json_key_location = ENV['JLOC']
        google.google_json_key_location = "/home/amgarcia/II/proz.json"


        # Configuración de la máquina.
        # Imagen: Ubuntu 16.04 LTS
        # Zona donde se ubica la VM: Oeste de Europa (Londres)
        # Nombre de la VM: ipcontainer
        # Características de la VM: 1 Core, 1,7GB de RAM y 10GB de HDD.
        google.image_family = 'ubuntu-1604-lts'
        google.zone = 'europe-west2-a'
        google.name = 'projectz'
        google.machine_type = 'g1-small'

        # Configuración del usuario y private_key para conectarme por SSH.
        override.ssh.username = 'amgarcia'
        override.ssh.private_key_path = '~/.ssh/google_compute_engine'
    end

    # Provisionamiento con un playbook de Ansible.
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision/playbook.yml"
    end
end
