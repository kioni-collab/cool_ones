<template>
  <div >
    <AdminOne/>
    <AdminTwo />
  </div>
</template>

<script>

import { ModalBus } from '../eventBus'


import AdminOne from './AdminOne'
import AdminTwo from './AdminTwo'
import Alert from './Alert'
import ModalRoot from './ModalRoot'

export default {
  name: 'Admin',
  components: {
    AdminOne,
    AdminTwo
  }

}
</script>