const API_BASE = '/api';

async function apiGetSpools(material = '', color = '', archived = false) {
    let url = `${API_BASE}/spools`;
    const params = [];

    if (material) params.push(`material=${encodeURIComponent(material)}`);
    if (color) params.push(`color=${encodeURIComponent(color)}`);
    if (archived) params.push(`archived=true`);

    if (params.length) url += '?' + params.join('&');

    const response = await fetch(url);
    if (!response.ok) throw new Error('Spulen konnten nicht geladen werden');
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
        throw new Error(error.error || 'Spool konnte nicht erstellt werden');
    }
    return response.json();
}

async function apiGetSpool(spoolId) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}`);
    if (!response.ok) throw new Error('Spool nicht gefunden');
    return response.json();
}

async function apiUpdateSpool(spoolId, data) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Spool konnte nicht aktualisiert werden');
    return response.json();
}

async function apiConsumeSpool(spoolId, grams) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}/consume`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grams })
    });
    if (!response.ok) throw new Error('Material konnte nicht verbraucht werden');
    return response.json();
}

async function apiArchiveSpool(spoolId) {
    const response = await fetch(`${API_BASE}/spools/${spoolId}/archive`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) throw new Error('Spool konnte nicht archiviert werden');
    return response.json();
}