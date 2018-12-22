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
    # VM.
    config.vm.box = "google/gce"

    config.vm.provider :google do |google, override|
        # ID del proyecto en google cloud platform.
        #google.google_project_id = ENV['ID_GCP']
        google.google_project_id ="projectz"

        # Email.
        #google.google_client_email = ENV['CEM']
        google.google_client_email = "iv-524@projectz.iam.gserviceaccount.com"

        # clave cuenta de servicio.
        #google.google_json_key_location = ENV['JLOC']
        google.google_json_key_location = "/home/amgarcia/II/proz.json"

        google.image_family = 'ubuntu-1604-lts'
        google.zone = 'europe-west2-a'
        google.name = 'projectz'
        google.machine_type = 'g1-small'

        # Configuración de usuario y clave privada para la conexión por SSH.
        override.ssh.username = 'amgarcia'
        override.ssh.private_key_path = '~/.ssh/google_compute_engine'
    end

    # Provisionamiento Ansible.
    config.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision/playbook.yml"
    end
end
