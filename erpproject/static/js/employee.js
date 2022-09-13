const first = document.querySelector('#home-tab');
const second = document.querySelector('#profile-tab');
const sFirst = document.querySelector('#home-tab-pane');
const sSecond = document.querySelector('#profile-tab-pane');

// function to add employee private info
function addFirst(e) {
    var html = 
    `   <div class="row mb-2">
            <!-- address -->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.address.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.address}}
                    </div>
                </div>
            </div>
            <!-- dob -->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.dob.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.dob}}
                    </div>
                </div>
            </div>
            <!-- nationality -->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.nationality.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.nationality}}
                    </div>
                </div>
            </div>
            <!-- marital status -->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.marital_status.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.marital_status}}
                    </div>
                </div>
            </div>
            <!-- gender_status-->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.gender_status.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.gender_status}}
                    </div>
                </div>
            </div>
            <!-- emergency_contact-->
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="{{ form.emergency_contact.id_for_label }}" class="col-sm-2 col-form-label col-form-label-sm">Address:</label>
                    <div class="col-sm-10">
                        {{form.emergency_contact}}
                    </div>
                </div>
            </div>
        </div>
    `;
    sFirst.innerHTML = html;
    e.preventDefault();
}

// function add employee academic info    
function addSecond(e) {
    var html = 
    `
        <div class="row mb-2">
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Bank Name:</label>
                    <div class="col-sm-10">
                    <input type="email" class="form-control" id="colFormLabelSm" placeholder="Zenith, First bank" name="vendor_bank" autocomplete="off">
                    </div>
                </div>
            </div>
            <div class="col-md-6">
                <div class="row mb-3">
                    <label for="colFormLabelSm" class="col-sm-2 col-form-label col-form-label-sm">Acc No:</label>
                    <div class="col-sm-10">
                    <input type="email" class="form-control" id="colFormLabelSm" placeholder="BE 0456 9846 1239" name="vendor_acc-no" autocomplete="off">
                    </div>
                </div>
            </div>
        </div>
    `;
    sSecond.innerHTML = html;
    e.preventDefault();
}

// attach event listener to employee onboarding(private info)
document.addEventListener('DOMContentLoaded', ()=>{
    first.onclick = addFirst
});

// set second event listener to employee onboarding(academic)
document.addEventListener('DOMContentLoaded', ()=>{
    second.onclick = addSecond
});