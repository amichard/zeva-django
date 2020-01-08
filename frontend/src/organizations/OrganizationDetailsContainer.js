/*
 * Container component
 * All data handling & manipulation should be handled here.
 */

import React, { useEffect, useState } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import OrganizationDetailsPage from './components/OrganizationDetailsPage';

const OrganizationDetailsContainer = (props) => {
  const [details, setDetails] = useState([]);
  const [loading, setLoading] = useState(true);
  const { keycloak } = props;

  const refreshDetails = () => {
    const { token } = keycloak;
    axios.get('http://localhost/api/users/current', {
      headers: { Authorization: `Bearer ${token}` },
    }).then((response) => {
      console.error(response);
    });
    // keycloak.updateToken(30).then(() => {
    //   const client = new OrganizationDetailsClient('http://localhost:10000/grpc');

    //   const request = new GetMyOrganizationRequest();

    //   const metadadta = {
    //     authorization: keycloak.idToken, // || token for auth token
    //   };

    //   const call = client.getMyOrganization(request, metadadta);

    //   call.on('data', (response) => {
    //     setDetails({
    //       name: response.getName(),
    //     });

    //     setLoading(false);
    //   });
    // });
  };

  useEffect(() => {
    refreshDetails();
  }, [keycloak.authenticated]);

  return (
    <OrganizationDetailsPage
      details={details}
      loading={loading}
    />
  );
};

OrganizationDetailsContainer.propTypes = {
  keycloak: PropTypes.shape().isRequired,
};

export default OrganizationDetailsContainer;
