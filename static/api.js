const API_BASE = '/api';

async function apiGetSpools(material = '', color = '', archived = false) {
    let url = `${API_BASE}/spools`;
    const params = [];

    if (material) params.push(`material=${encodeURIComponent(material)}`);
    if (color) params.push(`color=${encodeURIComponent(color)}`);
    if (archived) params.push(`archived=true`);

    if (params.length) url += '?' + params.join('&');

    const response = await fetch(url);
    if (!response.ok) throw new Error('Could not load spools');
    return response.json();
}

async function apiCreateSpool(data) {
    const response = await fetch(`${API_BASE}/spools`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.error || 'Could not create spool');
    }
    return response.json();
}

async function apiGetSpool(spoolId) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}`);
    if (!response.ok) throw new Error('Spool not found');
    return response.json();
}

async function apiUpdateSpool(spoolId, data) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Could not update spool');
    return response.json();
}

async function apiConsumeSpool(spoolId, grams) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}/consume`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grams })
    });
    if (!response.ok) throw new Error('Could not consume material');
    return response.json();
}

async function apiArchiveSpool(spoolId) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}/archive`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) throw new Error('Could not archive spool');
    return response.json();
}