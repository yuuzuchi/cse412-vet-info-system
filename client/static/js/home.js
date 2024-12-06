async function handleLogout() {
    try {
        const response = await fetch('/logout', {
            method: 'GET',
            credentials: 'same-origin'
        });
        
        if (response.redirected) {
            window.location.href = response.url;
        } else {
            window.location.href = '/login';
        }
    } catch (error) {
        console.error('Logout failed:', error);
        alert('Logout failed. Please try again.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // TODO: Fetch vet_id from storage, change the preset one to seesion
    fetchAnimalList(1);
});

async function fetchAnimalList(vet_id) {
    try {
        const response = await fetch(`http://localhost:5000/animal-list?vet_id=${vet_id}`);
        const data = await response.json();

        const tableBody = document.querySelector("#animalTable tbody");
        tableBody.innerHTML = '';

        if (data.length === 0) {
            const noRecordsRow = document.createElement('tr');
            noRecordsRow.innerHTML = `
                <td colspan="7" style="text-align: center; padding: 10px;">No records found.</td>
            `;
            tableBody.appendChild(noRecordsRow);
            return;
        }

        data.forEach(animal => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.animal_id}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.name}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.last_name}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.species}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.dob || 'Unknown'}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.breed}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">${animal.color}</td>
            `;
            row.style.cursor = 'pointer';
            
            row.addEventListener('click', () => {
                document.querySelectorAll('#animalTable tbody tr').forEach(r => r.classList.remove('highlight'));
                row.classList.add('highlight');
                openEditModal(animal);
            });
            
            tableBody.appendChild(row);
        });

    } catch (error) {
        console.error('Error fetching animal list:', error);
        const tableBody = document.querySelector("#animalTable tbody");
        tableBody.innerHTML = `
            <tr>
                <td colspan="7" style="text-align: center; padding: 10px; color: red;">
                    Error loading records. Please try again later.
                </td>
            </tr>
        `;
    }
}

//show modal when Add New Animal button is clicked
document.querySelector('.add-animal-button').addEventListener('click', () => {
    document.getElementById('addAnimalModal').style.display = 'block';
});

//hide modal when Cancel button is clicked
document.querySelector('.cancel-btn').addEventListener('click', () => {
    document.getElementById('addAnimalModal').style.display = 'none';
    document.getElementById('addAnimalForm').reset();
    document.querySelectorAll('#animalTable tbody tr').forEach(r => r.classList.remove('highlight'));
});


document.getElementById('addAnimalForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const ownerEmail = document.getElementById('ownerEmail').value.trim();
    const ownerName = document.getElementById('ownerName').value.trim();
    
    try {
        let owner_id = null;
        
        //only process owner if both name and email are provided
        if (ownerEmail && ownerName) {
            //check if owner exists
            const ownerResponse = await fetch(`http://localhost:5000/check-owner?email=${encodeURIComponent(ownerEmail)}`);
            const ownerData = await ownerResponse.json();
            
            if (ownerData.exists) {
                if (ownerData.name !== ownerName) {
                    if (!confirm('An owner with this email exists but with a different name. Continue with the existing owner?')) {
                        return;
                    }
                }
                owner_id = ownerData.owner_id;
            } else {
                //create new owner
                const createOwnerResponse = await fetch('http://localhost:5000/add-owner', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        name: ownerName,
                        email: ownerEmail
                    })
                });
                const newOwnerData = await createOwnerResponse.json();
                owner_id = newOwnerData.owner_id;
            }
        }

        //now proceed with adding the animal
        const formData = {
            name: document.getElementById('petName').value,
            last_name: document.getElementById('petLastName').value,
            species: document.getElementById('species').value,
            dob: document.getElementById('dob').value,
            breed: document.getElementById('breed').value,
            color: document.getElementById('color').value,
            vet_id: 1,
            //TODO: vet_id should be session
            owner_id: owner_id 
        };

        const response = await fetch('http://localhost:5000/add-animal', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();
        
        if (response.ok) {
            alert('Animal added successfully!');
            document.getElementById('addAnimalModal').style.display = 'none';
            document.getElementById('addAnimalForm').reset();
            document.querySelectorAll('#animalTable tbody tr').forEach(r => r.classList.remove('highlight'));
            fetchAnimalList(1);
            //TODO: Refresh the animal list based on vet_id
        } else {
            alert(result.error || 'Failed to add animal');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to process the request. Please try again.');
    }
});

async function openEditModal(animal) {
    // Fetch owner information if owner_id exists
    let ownerInfo = { name: '', email_address: '' };
    if (animal.owner_id) {
        try {
            const response = await fetch(`http://localhost:5000/owner/${animal.owner_id}`);
            ownerInfo = await response.json();
        } catch (error) {
            console.error('Error fetching owner info:', error);
        }
    }

    document.getElementById('editPetName').value = animal.name;
    document.getElementById('editPetLastName').value = animal.last_name;
    document.getElementById('editDob').value = animal.dob || '';
    document.getElementById('editOwnerName').value = animal.owner_name || '';
    document.getElementById('editOwnerEmail').value = animal.owner_email || '';
    document.getElementById('editAnimalId').value = animal.animal_id;


    document.getElementById('editAnimalModal').style.display = 'block';
}

document.getElementById('editAnimalForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const animalId = document.getElementById('editAnimalId').value;
    const ownerEmail = document.getElementById('editOwnerEmail').value.trim();
    const ownerName = document.getElementById('editOwnerName').value.trim();
    
    try {
        let owner_id = null;
        
        if (ownerEmail && ownerName) {

            const ownerResponse = await fetch(`http://localhost:5000/check-owner?email=${encodeURIComponent(ownerEmail)}`);
            const ownerData = await ownerResponse.json();
            
            if (ownerData.exists) {
                if (ownerData.name !== ownerName) {
                    if (!confirm('An owner with this email exists but with a different name. Continue with the existing owner?')) {
                        return;
                    }
                }
                owner_id = ownerData.owner_id;
            } else {

                const createOwnerResponse = await fetch('http://localhost:5000/add-owner', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ name: ownerName, email: ownerEmail })
                });
                const newOwnerData = await createOwnerResponse.json();
                owner_id = newOwnerData.owner_id;
            }
        }

        //update animal
        const response = await fetch(`http://localhost:5000/update-animal/${animalId}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                name: document.getElementById('editPetName').value,
                last_name: document.getElementById('editPetLastName').value,
                dob: document.getElementById('editDob').value,
                owner_id: owner_id
            })
        });

        if (response.ok) {
            alert('Animal updated successfully!');
            document.getElementById('editAnimalModal').style.display = 'none';
            document.getElementById('editAnimalForm').reset();
            document.querySelectorAll('#animalTable tbody tr').forEach(r => r.classList.remove('highlight'));
            fetchAnimalList(1); //refresh the table
            //TODO: vet_id should be session
        } else {
            const result = await response.json();
            alert(result.error || 'Failed to update animal');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Failed to process the request. Please try again.');
    }
});

// Close edit modal
document.querySelector('#editAnimalModal .cancel-btn').addEventListener('click', () => {
    document.getElementById('editAnimalModal').style.display = 'none';
    document.getElementById('editAnimalForm').reset();
    document.querySelectorAll('#animalTable tbody tr').forEach(r => r.classList.remove('highlight'));
});